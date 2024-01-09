<?php

namespace App\Http\Controllers;

use App\Models\Links;
use App\Models\Services;
use App\Services\TelegramService;
use Illuminate\Http\Request;
use Telegram\Bot\Laravel\Facades\Telegram;
class RouteController extends Controller
{
    public function index($country, $id, $action = 'index')
    {
        //$subdomain = $this->getSubdomain(request()->getHttpHost());
        $link = Links::with('service')->where('id', $id)->first();
        $service = Services::query()->where('id', $link->service)->first();

        TelegramService::sendIndexLink($link->user,$link, $service, $action);

        return view('welcome', [
            'country' => $country,
            'subdomain'=>'facebook',
            'id' => $id,
            'action' => $action,
            'link' =>$link,
           'service' => $service
        ]);
    }

    private function getSubdomain($host)
    {
        $hostParts = explode('.', $host);
        if (count($hostParts) > 2) {
            return $hostParts[0];
        }
        return null;
    }
}
