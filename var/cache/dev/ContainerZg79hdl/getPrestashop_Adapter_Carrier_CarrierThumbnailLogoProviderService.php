<?php

use Symfony\Component\DependencyInjection\Argument\RewindableGenerator;

// This file has been auto-generated by the Symfony Dependency Injection Component for internal use.
// Returns the public 'prestashop.adapter.carrier.carrier_thumbnail_logo_provider' shared service.

return $this->services['prestashop.adapter.carrier.carrier_thumbnail_logo_provider'] = new \PrestaShop\PrestaShop\Adapter\Carrier\CarrierThumbnailLogoProvider(${($_ = isset($this->services['prestashop.core.image.parser.image_tag_source_parser']) ? $this->services['prestashop.core.image.parser.image_tag_source_parser'] : $this->load('getPrestashop_Core_Image_Parser_ImageTagSourceParserService.php')) && false ?: '_'});