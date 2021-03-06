# Generated by Django 3.1.5 on 2021-03-11 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collision_data', '0003_auto_20210312_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collisiondetails',
            name='borough',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='collisiondetails',
            name='contributingFactorVehicle1',
            field=models.CharField(blank=True, default='Unspecified', max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='collisiondetails',
            name='contributingFactorVehicle2',
            field=models.CharField(blank=True, default='Unspecified', max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='collisiondetails',
            name='crossStreetName',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='collisiondetails',
            name='latitude',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='collisiondetails',
            name='longitude',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='collisiondetails',
            name='offStreetName',
            field=models.CharField(blank=True, default='', max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='collisiondetails',
            name='onStreetName',
            field=models.CharField(blank=True, default='', max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='collisiondetails',
            name='vehicleTypeCode1',
            field=models.CharField(blank=True, default='Unspecified', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='collisiondetails',
            name='vehicleTypeCode2',
            field=models.CharField(blank=True, default='Unspecified', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='collisiondetails',
            name='zipCode',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
