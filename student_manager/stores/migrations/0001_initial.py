# Generated by Django 4.0.5 on 2022-06-09 08:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import student_manager.stores.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('ordering_for', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='carts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=255)),
                ('last_name', models.CharField(blank=True, max_length=255)),
                ('mobile_number', models.CharField(blank=True, db_index=True, max_length=255)),
                ('address', models.CharField(blank=True, default='', max_length=255)),
                ('city', models.CharField(blank=True, default='', max_length=255)),
                ('province', models.CharField(blank=True, default='', max_length=255)),
                ('latitude', models.DecimalField(decimal_places=8, max_digits=11, null=True)),
                ('longitude', models.DecimalField(decimal_places=8, max_digits=11, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('brand', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, default='')),
                ('average_cost', models.DecimalField(decimal_places=4, default=0, max_digits=19)),
                ('status', models.CharField(blank=True, db_index=True, max_length=20, null=True)),
                ('sellable', models.BooleanField(default=False)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='StoreAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=255)),
                ('last_name', models.CharField(blank=True, max_length=255)),
                ('mobile_number', models.CharField(blank=True, db_index=True, max_length=255)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('city', models.CharField(blank=True, max_length=255)),
                ('province', models.CharField(blank=True, max_length=255)),
                ('latitude', models.DecimalField(decimal_places=8, max_digits=11, null=True)),
                ('longitude', models.DecimalField(decimal_places=8, max_digits=11, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=student_manager.stores.models.store_img_path)),
                ('name', models.CharField(max_length=255)),
                ('url', models.CharField(db_index=True, max_length=255, unique=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(max_length=255)),
                ('barangay', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('province', models.CharField(max_length=255)),
                ('landmark', models.TextField()),
                ('latitude', models.DecimalField(blank=True, decimal_places=8, max_digits=11, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=8, max_digits=11, null=True)),
                ('active', models.BooleanField(default=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='stores', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(db_index=True, max_length=32)),
                ('delivery_method', models.CharField(blank=True, choices=[('DELIVERY', 'Deliver'), ('PICKUP', 'Pickup')], db_index=True, max_length=32, null=True)),
                ('payment_status', models.CharField(choices=[('TO_COLLECT', 'To collect'), ('UNPAID', 'Unpaid'), ('PAID', 'Paid')], db_index=True, default='TO_COLLECT', max_length=20)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('FOR_APPROVAL', 'For approval'), ('FOR_PROCESSING', 'For processing'), ('PROCESSING', 'Processing'), ('FOR_DISPATCH', 'For Dispatch'), ('DISPATCHED', 'Dispatched'), ('ENROUTE', 'Enroute'), ('ARRIVED', 'Arrived'), ('RECEIVED', 'Received'), ('TO_PACK', 'To Pack'), ('CANCELED', 'Canceled'), ('REJECTED', 'Rejected'), ('COMPLETED', 'Completed'), ('DELIVERY_FAILED', 'Delivery Failed'), ('RETURNED', 'Returned')], db_index=True, default='PENDING', max_length=20)),
                ('total_discount_amount', models.IntegerField(default=0)),
                ('total_items_amount', models.IntegerField(default=0)),
                ('total_amount', models.IntegerField(default=0)),
                ('estimated_delivery_date', models.DateField(blank=True, db_index=True, null=True)),
                ('approved_at', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('canceled_at', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('received_at', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='stores.cart')),
                ('delivery_address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='stores.deliveryaddress')),
                ('store', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='stores.store')),
                ('store_address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='stores.storeaddress')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='store',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='carts', to='stores.store'),
        ),
    ]
