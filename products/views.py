"""Products Views"""
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import Http404
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.db.models.functions import Lower
from django.urls import reverse_lazy
from .models import Product, Category, ReviewRating
from .forms import ProductForm, ReviewForm
from favourites.models import Favourites


def error_403_view(request, exception):
    '''403 error view'''
    return render(request, '403.html', status=403)


def error_404_view(request, exception):
    '''404 error view'''
    return render(request, '404.html', status=404)


def error_500_view(request):
    """
    404 error view
    """
    return render(request, '500.html', status=500)


def all_products(request):
    """ A view to show individual product details """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               ("You didn't enter any search criteria!"))
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details"""

    product = get_object_or_404(Product, pk=product_id)
    review_form = ReviewForm(data=request.POST or None)
    reviews = ReviewRating.objects.filter(
        product=product).order_by('-created_on')
    total_reviews = reviews.count()
    rating_average = get_average_rating(reviews)
    Product.objects.filter(id=product.id).update(
        rating=rating_average)
    try:
        favourites = get_object_or_404(Favourites, username=request.user.id)
    except Http404:
        is_product_in_favourites = False
    else:
        is_product_in_favourites = bool(product in favourites.products.all())

    context = {
        'is_product_in_favourites': is_product_in_favourites,
        'product': product,
        'review_form': review_form,
        'reviews': reviews,
        'total_reviews': total_reviews,
        'rating_average': rating_average
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure \
                the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please \
                ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def submit_review(request, product_id):
    """ View to review a product """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)

        if review_form.is_valid():
            already_reviewed = ReviewRating.objects.filter(product=product,
                                                           user=request.user)
            if not already_reviewed:
                ReviewRating.objects.create(
                        product=product,
                        user=request.user,
                        subject=request.POST['subject'],
                        rating=request.POST['rating'],
                        review=request.POST['review'],
                )
                reviews = ReviewRating.objects.filter(product=product)
                rating_average = get_average_rating(reviews)
                Product.objects.filter(id=product.id).update(
                    rating=rating_average)
                messages.success(
                    request, 'Your review has been successfully added!')
            else:
                messages.error(request, 'You have already reviewed '
                                        'this product!')
            return redirect(reverse('product_detail', args=[product.id]))

        messages.error(request, 'Your review has not been submitted')
    messages.error(request, 'Invalid Method.')
    return redirect(reverse('product_detail', args=[product.id]))


class UpdateReviewView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    A view to edit a Review
    """
    model = ReviewRating
    form_class = ReviewForm
    template_name = "products/update_review.html"
    success_message = "Review has been updated"
    success_url = reverse_lazy('products')


class ReviewDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    '''
    View displays the option to delete the review to the user.
    '''
    model = ReviewRating
    template_name = 'products/delete_review.html'
    success_message = "Review has been deleted"
    success_url = reverse_lazy('products')


def get_average_rating(reviews):
    """
    Function to get the average rating of product
    from the reviews
    """
    total_reviews = 0
    ratings_total = 0
    rating_average = 0
    for review in reviews:
        total_reviews = total_reviews + 1
        ratings_total = ratings_total + review.rating

    if total_reviews > 0:
        average_rating = (ratings_total / total_reviews)
        rating_average = round(average_rating, 1)
        return rating_average
    else:
        return rating_average
