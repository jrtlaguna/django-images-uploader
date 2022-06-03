from PIL import Image as pillow

from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from images.models import Image


def index(request: HttpRequest) -> HttpResponse:
    template_name = "images/home.html"
    if request.method == "POST":
        try:
            images_list = []
            for f in request.FILES.getlist("image"):
                img = pillow.open(f)
                img.verify()
                print(f)
                images_list.append(Image(image=f))
            Image.objects.bulk_create(images_list)
        except Exception as err:
            print(err)
            messages.error(request, f"{f} is not a valid image.")

        images = Image.objects.filter(status=Image.ImageStatus.ACTIVE).order_by(
            "created_at"
        )
        ctx = {"images": images}
        return render(request, "images/partials/image_list.html", ctx)
    else:
        images = Image.objects.filter(status=Image.ImageStatus.ACTIVE)
    ctx = {"images": images, "page": "index"}

    return render(request, template_name, ctx)


def show_active(request: HttpRequest) -> HttpResponse:
    images = Image.objects.filter(status=Image.ImageStatus.ACTIVE)
    ctx = {"images": images, "page": "archived"}

    return render(request, "images/partials/image_list.html", ctx)


def show_archived(request: HttpRequest) -> HttpResponse:

    images = Image.objects.filter(status=Image.ImageStatus.ARCHIVED)
    ctx = {"images": images, "page": "archived"}

    return render(request, "images/partials/image_list.html", ctx)


def show_deleted(request: HttpRequest) -> HttpResponse:

    images = Image.objects.filter(status=Image.ImageStatus.DELETED)
    ctx = {"images": images, "page": "deleted"}

    return render(request, "images/partials/image_list.html", ctx)


def archive_image(request: HttpRequest, image_id: int) -> HttpResponse:
    if image_id:
        try:
            image = Image.objects.get(id=image_id)
            image.status = Image.ImageStatus.ARCHIVED
            image.save()
        except Image.DoesNotExist:
            return redirect("images:index")
    ctx = {}
    ctx["images"] = Image.objects.filter(status=Image.ImageStatus.ACTIVE).order_by(
        "created_at"
    )
    return render(request, "images/partials/image_list.html", ctx)


def delete_image(request: HttpRequest, image_id: int) -> HttpResponse:
    if image_id:
        try:
            image = Image.objects.get(id=image_id)
            image.status = Image.ImageStatus.DELETED
            image.save()
        except Image.DoesNotExist:
            print("Image does not exist.")
    ctx = {}
    ctx["images"] = Image.objects.filter(status=Image.ImageStatus.ACTIVE).order_by(
        "created_at"
    )
    return render(request, "images/partials/image_list.html", ctx)
