<?php

use Symfony\Component\DependencyInjection\Argument\RewindableGenerator;

// This file has been auto-generated by the Symfony Dependency Injection Component for internal use.
// Returns the public 'form.type.sell.product.pricing.pricing_type' shared service.

return $this->services['form.type.sell.product.pricing.pricing_type'] = new \PrestaShopBundle\Form\Admin\Sell\Product\Pricing\PricingType(${($_ = isset($this->services['translator.default']) ? $this->services['translator.default'] : $this->getTranslator_DefaultService()) && false ?: '_'}, ${($_ = isset($this->services['prestashop.adapter.legacy.context']) ? $this->services['prestashop.adapter.legacy.context'] : $this->getPrestashop_Adapter_Legacy_ContextService()) && false ?: '_'}->getLanguages(), ${($_ = isset($this->services['prestashop.core.form.choice_provider.tax_rule_group_choice_provider']) ? $this->services['prestashop.core.form.choice_provider.tax_rule_group_choice_provider'] : ($this->services['prestashop.core.form.choice_provider.tax_rule_group_choice_provider'] = new \PrestaShop\PrestaShop\Adapter\Form\ChoiceProvider\TaxRuleGroupChoiceProvider())) && false ?: '_'}->getChoices(), ${($_ = isset($this->services['prestashop.core.form.choice_provider.tax_rule_group_choice_provider']) ? $this->services['prestashop.core.form.choice_provider.tax_rule_group_choice_provider'] : ($this->services['prestashop.core.form.choice_provider.tax_rule_group_choice_provider'] = new \PrestaShop\PrestaShop\Adapter\Form\ChoiceProvider\TaxRuleGroupChoiceProvider())) && false ?: '_'}->getChoicesAttributes(), ${($_ = isset($this->services['prestashop.adapter.data_provider.currency']) ? $this->services['prestashop.adapter.data_provider.currency'] : $this->getPrestashop_Adapter_DataProvider_CurrencyService()) && false ?: '_'}->getDefaultCurrency(), ${($_ = isset($this->services['prestashop.router']) ? $this->services['prestashop.router'] : $this->load('getPrestashop_RouterService.php')) && false ?: '_'});
