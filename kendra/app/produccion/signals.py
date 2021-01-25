# from django.db.models.signals import pre_save, post_save
# from django.dispatch import receiver
# from .models import *


# # def new_gramos(instance, new_gramo: int = None):
# #     """ Recursive unique property generator """

# #     instance_model = instance.__class__

# #     last_property = instance_model.objects.last()

# #     last_id = 1 if not last_property or not last_property.id_property else last_property.id_property

# #     id_property = last_id if new_id is None else new_id

# #     # Verify if the id_property_exists already exists

# #     id_property_exists = instance_model.objects.filter(
# #         gramos=gramos).exists()

# #     if id_property_exists:
# #         new_id = id_property + 1
# #         return new_gramos(instance, new_id=new_id)

# #     return gramos


# @receiver(post_save, sender=DetalleProducion)
# def set_gramos(sender, instance, created, **kwargs):
#     """ Sets the nuevos gramos """
#     print("Esta por aqui en el set gramos")
#     if created:
#         print("Se creo el dato")
#     # if not instance.gramos:
#     #     instance.gramos = new_gramos(instance)
