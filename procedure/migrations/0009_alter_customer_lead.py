# Generated by Django 4.2 on 2024-10-01 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('procedure', '0008_alter_customer_created_at_alter_customer_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='lead',
            field=models.CharField(choices=[('دیسپچ سرو', 'دیسپچ سرو'), ('دیسپچ سپیدز', 'دیسپچ سپیدز'), ('مشتریان', 'مشتریان'), ('اینترنت', 'اینترنت'), ('وبسایت', 'وبسایت'), ('راه\u200cانداز', 'راه\u200cانداز')], default='دیسپچ سرو', max_length=50),
        ),
    ]