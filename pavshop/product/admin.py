from django.contrib import admin
from .forms import ProductVersionReviewAdminForm
from .models import (
    Color,
    Designer,
    Brand,
    Discount,
    ProductCategory,
    ProductTag,
    Product,
    ProductVersion,
    ProductVersionImage,
    ProductVersionReview,
    Wishlist
)


# Register your models here.


# ========== Inline ==========
class DiscountInline(admin.TabularInline):
    model = Discount.products.through
    extra = 1
    verbose_name = "Discount"
    verbose_name_plural = "Discounts"


class ProductVersionImageInline(admin.TabularInline):
    model = ProductVersionImage
    extra = 1
    verbose_name = "Image"
    verbose_name_plural = "Images"
# ========== END Inline ==========


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "is_active", "created_at", "updated_at"]
    list_display_links = ["id", "name"]
    list_editable = ["is_active"]
    list_filter = ["is_active"]
    search_fields = ["name"]


@admin.register(Designer)
class DesignerAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "is_active", "created_at", "updated_at"]
    list_display_links = ["id", "name"]
    list_editable = ["is_active"]
    list_filter = ["is_active"]
    search_fields = ["name"]


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "is_active", "created_at", "updated_at"]
    list_display_links = ["id", "name"]
    list_editable = ["is_active"]
    list_filter = ["is_active"]
    search_fields = ["name"]


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    fields = ["name", "percent", "is_active", "products"]
    filter_horizontal = ["products"]

    list_display = ["id", "name", "get_percent",
                    "is_active", "created_at", "updated_at"]
    list_display_links = ["id", "name"]
    list_editable = ["is_active"]
    list_filter = ["is_active"]
    search_fields = ["name"]

    def get_percent(self, obj):
        return f"{obj.percent}%"
    get_percent.admin_order_field = "percent"
    get_percent.short_description = "Percent"


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "is_active",
                    "slug", "created_at", "updated_at"]
    list_display_links = ["id", "name"]
    list_editable = ["is_active"]
    list_filter = ["is_active"]
    search_fields = ["name"]


@admin.register(ProductTag)
class ProductTagAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "is_active",
                    "slug", "created_at", "updated_at"]
    list_display_links = ["id", "name"]
    list_editable = ["is_active"]
    list_filter = ["is_active"]
    search_fields = ["name"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    filter_horizontal = ["product_categories", "product_tags"]

    list_display = ["id", "title", "brand", "get_categories",
                    "get_tags", "created_at", "updated_at"]
    list_display_links = ["id", "title"]
    list_filter = ["brand", "product_categories", "product_tags"]
    search_fields = ["title", "brand"]

    def get_categories(self, obj):
        arr = []
        for category in obj.product_categories.all():
            arr.append(category)
        return arr
    get_categories.short_description = "Categories"

    def get_tags(self, obj):
        arr = []
        for tag in obj.product_tags.all():
            arr.append(tag)
        return arr
    get_tags.short_description = "Tags"


@admin.register(ProductVersion)
class ProductVersionAdmin(admin.ModelAdmin):
    inlines = [DiscountInline, ProductVersionImageInline]
    filter_horizontal = ["colors"]

    list_display = ["id", "product", "designer", "price", "quantity",
                    "is_active", "get_colors", "get_discounts", "created_at", "updated_at"]
    list_display_links = ["id", "product"]
    list_filter = ["is_active", "product",
                   "colors", "created_at", "updated_at"]
    search_fields = ["product__title", "designer"]

    def get_colors(self, obj):
        arr = []
        for color in obj.colors.all():
            arr.append(color)
        return arr
    get_colors.short_description = "Colors"

    def get_discounts(self, obj):
        arr = []
        for discount in obj.discounts.all():
            arr.append(f"{discount.percent}%")
        return arr
    get_discounts.short_description = "Discounts"


@admin.register(ProductVersionImage)
class ProductVersionImageAdmin(admin.ModelAdmin):
    list_display = ["id", "product_version", "is_active",
                    "image", "created_at", "updated_at"]
    list_display_links = ["id", "product_version"]
    list_filter = ["is_active", "product_version"]


@admin.register(ProductVersionReview)
class ProductVersionReviewAdmin(admin.ModelAdmin):
    form = ProductVersionReviewAdminForm

    list_display = ["id", "product_version", "user",
                    "full_name", "email", "created_at", "updated_at"]
    list_display_links = ["id", "product_version"]
    list_filter = ["product_version", "user", "created_at", "updated_at"]
    search_fields = ["user__username", "user__first_name",
                     "user__last_name", "full_name", "email"]


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    filter_horizontal = ["product_versions"]

    list_display = ["user", "created_at", "updated_at"]
    search_fields = ["user__username"]
