"""Products Views"""
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, ReviewRating
from .forms import ProductForm, ReviewForm
from favourites.models import Favourites


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

        queries = Q(name__icontains=query) | Q(description__icontains=query)
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
    reviews = ReviewRating.objects.filter(product=product).order_by('-created_on')

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
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
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
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
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
                messages.info(request, 'Successfully added a review!')
            else:
                messages.error(request, 'You have already reviewed '
                                        'this product!')
            return redirect(reverse('product_detail', args=[product.id]))

        messages.error(request, 'Your review has not been submitted')
    messages.error(request, 'Invalid Method.')
    return redirect(reverse('product_detail', args=[product.id]))

    # if request.method == "POST":
    #     try:
    #         reviews = ReviewRating.objects.get(user=request.user, product=product)
    #         form = ReviewForm(request.POST, instance=reviews)
    #         form.save()
    #         messages.success(request, 'Your review has been updated!')
    #         return redirect(url)
    #     except ReviewRating.DoesNotExist:
    #         form = ReviewForm(request.POST)
    #         if form.is_valid():
    #             data = ReviewForm()
    #             data.subject = form.cleaned_data['subject']
    #             data.review = form.cleaned_data['review']
    #             data.rating = form.cleaned_data['rating']
    #             data.product = product
    #             data.user = request.user
    #             data.save()
    #             messages.success(request, 'Your review has been Submitted!')
    #             return redirect(url)
