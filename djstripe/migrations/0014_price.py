# Generated by Django 3.0.7 on 2020-06-11 18:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import djstripe.enums
import djstripe.fields


class Migration(migrations.Migration):

    dependencies = [
        ("djstripe", "0013_auto_20200611_1539"),
    ]

    operations = [
        migrations.CreateModel(
            name="Price",
            fields=[
                (
                    "djstripe_id",
                    models.BigAutoField(
                        primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("id", djstripe.fields.StripeIdField(max_length=255, unique=True)),
                (
                    "livemode",
                    models.BooleanField(
                        blank=True,
                        default=None,
                        help_text="Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation.",
                        null=True,
                    ),
                ),
                (
                    "created",
                    djstripe.fields.StripeDateTimeField(
                        blank=True,
                        help_text="The datetime this object was created in stripe.",
                        null=True,
                    ),
                ),
                (
                    "metadata",
                    djstripe.fields.JSONField(
                        blank=True,
                        help_text="A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format.",
                        null=True,
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, help_text="A description of this object.", null=True
                    ),
                ),
                ("djstripe_created", models.DateTimeField(auto_now_add=True)),
                ("djstripe_updated", models.DateTimeField(auto_now=True)),
                (
                    "active",
                    models.BooleanField(
                        help_text="Whether the price can be used for new purchases."
                    ),
                ),
                (
                    "currency",
                    djstripe.fields.StripeCurrencyCodeField(
                        help_text="Three-letter ISO currency code", max_length=3
                    ),
                ),
                (
                    "nickname",
                    models.CharField(
                        blank=True,
                        help_text="A brief description of the plan, hidden from customers.",
                        max_length=250,
                    ),
                ),
                (
                    "recurring",
                    djstripe.fields.JSONField(
                        blank=True,
                        help_text="The recurring components of a price such as `interval` and `usage_type`.",
                        null=True,
                    ),
                ),
                (
                    "type",
                    djstripe.fields.StripeEnumField(
                        enum=djstripe.enums.PriceType,
                        help_text="Whether the price is for a one-time purchase or a recurring (subscription) purchase.",
                        max_length=9,
                    ),
                ),
                (
                    "unit_amount",
                    djstripe.fields.StripeQuantumCurrencyAmountField(
                        blank=True,
                        help_text="The unit amount in cents to be charged, represented as a whole integer if possible. Null if a sub-cent precision is required.",
                        null=True,
                    ),
                ),
                (
                    "unit_amount_decimal",
                    djstripe.fields.StripeDecimalCurrencyAmountField(
                        blank=True,
                        decimal_places=12,
                        help_text="The unit amount in cents to be charged, represented as a decimal string with at most 12 decimal places.",
                        max_digits=19,
                        null=True,
                    ),
                ),
                (
                    "aggregate_usage",
                    djstripe.fields.StripeEnumField(
                        blank=True,
                        enum=djstripe.enums.PlanAggregateUsage,
                        help_text="Specifies a usage aggregation strategy for plans of usage_type=metered. Allowed values are `sum` for summing up all usage during a period, `last_during_period` for picking the last usage record reported within a period, `last_ever` for picking the last usage record ever (across period bounds) or max which picks the usage record with the maximum reported usage during a period. Defaults to `sum`.",
                        max_length=18,
                    ),
                ),
                (
                    "billing_scheme",
                    djstripe.fields.StripeEnumField(
                        blank=True,
                        enum=djstripe.enums.BillingScheme,
                        help_text="Describes how to compute the price per period. Either `per_unit` or `tiered`. `per_unit` indicates that the fixed amount (specified in amount) will be charged per unit in quantity (for plans with `usage_type=licensed`), or per unit of total usage (for plans with `usage_type=metered`). `tiered` indicates that the unit pricing will be computed using a tiering strategy as defined using the tiers and tiers_mode attributes.",
                        max_length=8,
                    ),
                ),
                (
                    "tiers",
                    djstripe.fields.JSONField(
                        blank=True,
                        help_text="Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`.",
                        null=True,
                    ),
                ),
                (
                    "tiers_mode",
                    djstripe.fields.StripeEnumField(
                        blank=True,
                        enum=djstripe.enums.PlanTiersMode,
                        help_text="Defines if the tiering price should be `graduated` or `volume` based. In `volume`-based tiering, the maximum quantity within a period determines the per unit price, in `graduated` tiering pricing can successively change as the quantity grows.",
                        max_length=9,
                        null=True,
                    ),
                ),
                (
                    "transform_usage",
                    djstripe.fields.JSONField(
                        blank=True,
                        help_text="Apply a transformation to the reported usage or set quantity before computing the billed price. Cannot be combined with `tiers`.",
                        null=True,
                    ),
                ),
                (
                    "trial_period_days",
                    models.IntegerField(
                        help_text="Number of trial period days granted when subscribing a customer to this plan. Null if no trial period is present.",
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "djstripe_owner_account",
                    djstripe.fields.StripeForeignKey(
                        blank=True,
                        help_text="The Stripe Account this object belongs to.",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="djstripe.Account",
                        to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
                    ),
                ),
                (
                    "product",
                    djstripe.fields.StripeForeignKey(
                        help_text="The product this price is associated with.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="prices",
                        to="djstripe.Product",
                        to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
                    ),
                ),
            ],
            options={"get_latest_by": "created", "abstract": False},
        ),
    ]
