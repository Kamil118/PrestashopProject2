<?php

use Symfony\Component\DependencyInjection\Argument\RewindableGenerator;

// This file has been auto-generated by the Symfony Dependency Injection Component for internal use.
// Returns the public 'prestashop.adapter.order.command_handler.send_process_order_email_handler' shared service.

return $this->services['prestashop.adapter.order.command_handler.send_process_order_email_handler'] = new \PrestaShop\PrestaShop\Adapter\Order\CommandHandler\SendProcessOrderEmailHandler(${($_ = isset($this->services['translator']) ? $this->services['translator'] : $this->getTranslatorService()) && false ?: '_'}, ${($_ = isset($this->services['prestashop.adapter.legacy.context']) ? $this->services['prestashop.adapter.legacy.context'] : $this->getPrestashop_Adapter_Legacy_ContextService()) && false ?: '_'}->getContext()->link);