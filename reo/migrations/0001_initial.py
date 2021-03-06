# *********************************************************************************
# REopt, Copyright (c) 2019-2020, Alliance for Sustainable Energy, LLC.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice, this list
# of conditions and the following disclaimer.
#
# Redistributions in binary form must reproduce the above copyright notice, this
# list of conditions and the following disclaimer in the documentation and/or other
# materials provided with the distribution.
#
# Neither the name of the copyright holder nor the names of its contributors may be
# used to endorse or promote products derived from this software without specific
# prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
# OF THE POSSIBILITY OF SUCH DAMAGE.
# *********************************************************************************
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields
import picklefield.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BadPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('run_uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('post', picklefield.fields.PickledObjectField(editable=False)),
                ('errors', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ElectricTariffModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('run_uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('urdb_utilty_name', models.TextField(default=b'', blank=True)),
                ('urdb_rate_name', models.TextField(default=b'', blank=True)),
                ('urdb_label', models.TextField(default=b'', blank=True)),
                ('blended_monthly_rates_us_dollars_per_kwh', django.contrib.postgres.fields.ArrayField(default=[], base_field=models.FloatField(blank=True), size=None)),
                ('blended_monthly_demand_charges_us_dollars_per_kw', django.contrib.postgres.fields.ArrayField(default=[], base_field=models.FloatField(blank=True), size=None)),
                ('net_metering_limit_kw', models.FloatField()),
                ('interconnection_limit_kw', models.FloatField()),
                ('wholesale_rate_us_dollars_per_kwh', models.FloatField()),
                ('urdb_response', picklefield.fields.PickledObjectField(null=True, editable=False)),
                ('year_one_energy_cost_us_dollars', models.FloatField(null=True, blank=True)),
                ('year_one_demand_cost_us_dollars', models.FloatField(null=True, blank=True)),
                ('year_one_fixed_cost_us_dollars', models.FloatField(null=True, blank=True)),
                ('year_one_min_charge_adder_us_dollars', models.FloatField(null=True, blank=True)),
                ('year_one_energy_cost_bau_us_dollars', models.FloatField(null=True, blank=True)),
                ('year_one_demand_cost_bau_us_dollars', models.FloatField(null=True, blank=True)),
                ('year_one_fixed_cost_bau_us_dollars', models.FloatField(null=True, blank=True)),
                ('year_one_min_charge_adder_bau_us_dollars', models.FloatField(null=True, blank=True)),
                ('total_energy_cost_us_dollars', models.FloatField(null=True, blank=True)),
                ('total_demand_cost_us_dollars', models.FloatField(null=True, blank=True)),
                ('total_fixed_cost_us_dollars', models.FloatField(null=True, blank=True)),
                ('total_min_charge_adder_us_dollars', models.FloatField(null=True, blank=True)),
                ('total_energy_cost_bau_us_dollars', models.FloatField(null=True, blank=True)),
                ('total_demand_cost_bau_us_dollars', models.FloatField(null=True, blank=True)),
                ('total_fixed_cost_bau_us_dollars', models.FloatField(null=True, blank=True)),
                ('total_min_charge_adder_bau_us_dollars', models.FloatField(null=True, blank=True)),
                ('year_one_bill_us_dollars', models.FloatField(null=True, blank=True)),
                ('year_one_bill_bau_us_dollars', models.FloatField(null=True, blank=True)),
                ('year_one_export_benefit_us_dollars', models.FloatField(null=True, blank=True)),
                ('year_one_energy_cost_series_us_dollars_per_kwh', django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.FloatField(null=True, blank=True), blank=True)),
                ('year_one_demand_cost_series_us_dollars_per_kw', django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.FloatField(null=True, blank=True), blank=True)),
                ('year_one_to_load_series_kw', django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.FloatField(null=True, blank=True), blank=True)),
                ('year_one_to_battery_series_kw', django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.FloatField(null=True, blank=True), blank=True)),
                ('year_one_energy_supplied_kwh', models.FloatField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='FinancialModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('run_uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('analysis_years', models.IntegerField()),
                ('escalation_pct', models.FloatField()),
                ('om_cost_escalation_pct', models.FloatField()),
                ('offtaker_discount_pct', models.FloatField()),
                ('offtaker_tax_pct', models.FloatField()),
                ('owner_discount_pct', models.FloatField(null=True)),
                ('owner_tax_pct', models.FloatField(null=True)),
                ('lcc_us_dollars', models.FloatField(null=True, blank=True)),
                ('lcc_bau_us_dollars', models.FloatField(null=True, blank=True)),
                ('npv_us_dollars', models.FloatField(null=True, blank=True)),
                ('net_capital_costs_plus_om_us_dollars', models.FloatField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='LoadProfileModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('run_uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('doe_reference_name', models.TextField(default=b'', null=True, blank=True)),
                ('annual_kwh', models.FloatField(null=True, blank=True)),
                ('year', models.IntegerField(default=2018)),
                ('monthly_totals_kwh', django.contrib.postgres.fields.ArrayField(default=[], base_field=models.FloatField(blank=True), size=None)),
                ('loads_kw', django.contrib.postgres.fields.ArrayField(default=[], base_field=models.FloatField(blank=True), size=None)),
                ('outage_start_hour', models.IntegerField(null=True, blank=True)),
                ('outage_end_hour', models.IntegerField(null=True, blank=True)),
                ('critical_load_pct', models.FloatField()),
                ('year_one_electric_load_series_kw', django.contrib.postgres.fields.ArrayField(default=[], base_field=models.FloatField(null=True, blank=True), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='MessageModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message_type', models.TextField(default=b'', blank=True)),
                ('message', models.TextField(default=b'', blank=True)),
                ('run_uuid', models.UUIDField(default=uuid.uuid4)),
                ('description', models.TextField(default=b'', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PVModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('run_uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('min_kw', models.FloatField()),
                ('max_kw', models.FloatField()),
                ('installed_cost_us_dollars_per_kw', models.FloatField()),
                ('om_cost_us_dollars_per_kw', models.FloatField()),
                ('macrs_option_years', models.IntegerField()),
                ('macrs_bonus_pct', models.FloatField()),
                ('macrs_itc_reduction', models.FloatField()),
                ('federal_itc_pct', models.FloatField()),
                ('state_ibi_pct', models.FloatField()),
                ('state_ibi_max_us_dollars', models.FloatField()),
                ('utility_ibi_pct', models.FloatField()),
                ('utility_ibi_max_us_dollars', models.FloatField()),
                ('federal_rebate_us_dollars_per_kw', models.FloatField()),
                ('state_rebate_us_dollars_per_kw', models.FloatField()),
                ('state_rebate_max_us_dollars', models.FloatField()),
                ('utility_rebate_us_dollars_per_kw', models.FloatField()),
                ('utility_rebate_max_us_dollars', models.FloatField()),
                ('pbi_us_dollars_per_kwh', models.FloatField()),
                ('pbi_max_us_dollars', models.FloatField()),
                ('pbi_years', models.FloatField()),
                ('pbi_system_max_kw', models.FloatField()),
                ('degradation_pct', models.FloatField(null=True, blank=True)),
                ('azimuth', models.FloatField()),
                ('losses', models.FloatField()),
                ('array_type', models.IntegerField()),
                ('module_type', models.IntegerField()),
                ('gcr', models.FloatField()),
                ('dc_ac_ratio', models.FloatField()),
                ('inv_eff', models.FloatField()),
                ('radius', models.FloatField()),
                ('tilt', models.FloatField()),
                ('size_kw', models.FloatField(null=True, blank=True)),
                ('average_yearly_energy_produced_kwh', models.FloatField(null=True, blank=True)),
                ('average_yearly_energy_exported_kwh', models.FloatField(null=True, blank=True)),
                ('year_one_energy_produced_kwh', models.FloatField(null=True, blank=True)),
                ('year_one_power_production_series_kw', django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.FloatField(null=True, blank=True), blank=True)),
                ('year_one_to_battery_series_kw', django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.FloatField(null=True, blank=True), blank=True)),
                ('year_one_to_load_series_kw', django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.FloatField(null=True, blank=True), blank=True)),
                ('year_one_to_grid_series_kw', django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.FloatField(null=True, blank=True), blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ScenarioModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('run_uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('api_version', models.TextField(default=b'', null=True, blank=True)),
                ('user_id', models.TextField(null=True, blank=True)),
                ('status', models.TextField(null=True, blank=True)),
                ('timeout_seconds', models.IntegerField(default=295)),
                ('time_steps_per_hour', models.IntegerField(default=8760)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SiteModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('run_uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('land_acres', models.FloatField(null=True, blank=True)),
                ('roof_squarefeet', models.FloatField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='StorageModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('run_uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('min_kw', models.FloatField()),
                ('max_kw', models.FloatField()),
                ('min_kwh', models.FloatField()),
                ('max_kwh', models.FloatField()),
                ('internal_efficiency_pct', models.FloatField()),
                ('inverter_efficiency_pct', models.FloatField()),
                ('rectifier_efficiency_pct', models.FloatField()),
                ('soc_min_pct', models.FloatField()),
                ('soc_init_pct', models.FloatField()),
                ('canGridCharge', models.BooleanField()),
                ('installed_cost_us_dollars_per_kw', models.FloatField()),
                ('installed_cost_us_dollars_per_kwh', models.FloatField()),
                ('replace_cost_us_dollars_per_kw', models.FloatField()),
                ('replace_cost_us_dollars_per_kwh', models.FloatField()),
                ('inverter_replacement_year', models.IntegerField()),
                ('battery_replacement_year', models.IntegerField()),
                ('macrs_option_years', models.IntegerField()),
                ('macrs_bonus_pct', models.FloatField()),
                ('macrs_itc_reduction', models.FloatField()),
                ('total_itc_pct', models.IntegerField()),
                ('total_rebate_us_dollars_per_kw', models.IntegerField()),
                ('size_kw', models.FloatField(null=True, blank=True)),
                ('size_kwh', models.FloatField(null=True, blank=True)),
                ('year_one_to_load_series_kw', django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.FloatField(null=True, blank=True), blank=True)),
                ('year_one_to_grid_series_kw', django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.FloatField(null=True, blank=True), blank=True)),
                ('year_one_soc_series_pct', django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.FloatField(null=True, blank=True), blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='URDBError',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.TextField(default=b'', blank=True)),
                ('type', models.TextField(default=b'', blank=True)),
                ('message', models.TextField(default=b'', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='WindModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('run_uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('min_kw', models.FloatField()),
                ('max_kw', models.FloatField()),
                ('installed_cost_us_dollars_per_kw', models.FloatField()),
                ('om_cost_us_dollars_per_kw', models.FloatField()),
                ('macrs_option_years', models.IntegerField()),
                ('macrs_bonus_pct', models.FloatField()),
                ('macrs_itc_reduction', models.FloatField()),
                ('federal_itc_pct', models.FloatField()),
                ('state_ibi_pct', models.FloatField()),
                ('state_ibi_max_us_dollars', models.FloatField()),
                ('utility_ibi_pct', models.FloatField()),
                ('utility_ibi_max_us_dollars', models.FloatField()),
                ('federal_rebate_us_dollars_per_kw', models.FloatField()),
                ('state_rebate_us_dollars_per_kw', models.FloatField()),
                ('state_rebate_max_us_dollars', models.FloatField()),
                ('utility_rebate_us_dollars_per_kw', models.FloatField()),
                ('utility_rebate_max_us_dollars', models.FloatField()),
                ('pbi_us_dollars_per_kwh', models.FloatField()),
                ('pbi_max_us_dollars', models.FloatField()),
                ('pbi_years', models.FloatField()),
                ('pbi_system_max_kw', models.FloatField()),
                ('size_kw', models.FloatField(null=True, blank=True)),
                ('average_yearly_energy_produced_kwh', models.FloatField(null=True, blank=True)),
                ('average_yearly_energy_exported_kwh', models.FloatField(null=True, blank=True)),
                ('year_one_energy_produced_kwh', models.FloatField(null=True, blank=True)),
                ('year_one_power_production_series_kw', django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.FloatField(null=True, blank=True), blank=True)),
                ('year_one_to_battery_series_kw', django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.FloatField(null=True, blank=True), blank=True)),
                ('year_one_to_load_series_kw', django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.FloatField(null=True, blank=True), blank=True)),
                ('year_one_to_grid_series_kw', django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.FloatField(null=True, blank=True), blank=True)),
            ],
        ),
    ]
