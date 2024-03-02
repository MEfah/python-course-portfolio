from blog.models import ContactInfo


def contact_info_list(request):
    return {"contact_info_list": ContactInfo.objects.all()}
