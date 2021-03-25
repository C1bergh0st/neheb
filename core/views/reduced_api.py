from django.shortcuts import render, get_object_or_404
from django.views.generic import View
import hashlib
from core.forms import UserForm
from django.http import HttpResponseBadRequest, HttpResponseForbidden, HttpResponse
from core.models import Secret, Tag, Transaction, Item
from pinax.eventlog.models import log
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.utils.decorators import method_decorator
import json

@method_decorator(csrf_exempt, name='dispatch')
class TransactionView(View):

    def post(self, request, **kwargs):
        tag_id = request.POST.get("tag_id")
        amount = request.POST.get("amount")
        item_id = request.POST.get("item_id")
        hash = request.POST.get("hash")
        if None in [tag_id, amount, item_id, hash]:
            return HttpResponseBadRequest("The request was malformed.")
        for secret in Secret.objects.all():
            calc_string = str(tag_id) + str(amount) + str(item_id) + str(secret.value)
            calc_hash = hashlib.sha256(calc_string.encode("ascii")).hexdigest()
            print(calc_string)
            print(calc_hash.upper())
            print(hash)
            if calc_hash.upper() == hash.upper():
                tag = get_object_or_404(Tag, pk=tag_id)
                item = get_object_or_404(Item, pk=item_id)
                transaction = Transaction(owner=tag.attendee, item=item, amount=amount)
                transaction.save()
                return HttpResponse("Success")
        log(
            user=request.user,
            action="attempted_break_in",
            extra={
                "REMOTE_ADDR": request.META.get('REMOTE_ADDR'),
                "body": str(request.body),
            }
        )
        return HttpResponseForbidden("Unauthorized attempt, this has been logged")

    def get(self, request, **kwargs):
        return HttpResponse("No POST")
