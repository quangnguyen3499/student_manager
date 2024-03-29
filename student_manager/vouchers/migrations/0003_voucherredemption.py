# Generated by Django 3.2.8 on 2022-06-14 09:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0005_alter_product_unique_together'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vouchers', '0002_voucheruser'),
    ]

    operations = [
        migrations.CreateModel(
            name='VoucherRedemption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('redeemed_at', models.DateTimeField(auto_now=True, null=True)),
                ('discount_amount', models.IntegerField()),
                ('cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='voucher_redemptions', to='stores.cart')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='voucher_redemptions', to='stores.order')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('voucher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='redemptions', to='vouchers.voucher')),
            ],
        ),
    ]
