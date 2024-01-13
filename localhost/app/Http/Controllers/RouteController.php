<?php

namespace App\Http\Controllers;

use App\Models\Links;
use App\Models\Logs;
use App\Models\Services;
use App\Models\Users;
use App\Services\TelegramService;
use Illuminate\Http\Request;
use Telegram\Bot\Laravel\Facades\Telegram;
class RouteController extends Controller
{
    public function index($country, $id, $action = 'index')
    {
        $subdomain = $this->getSubdomain(request()->getHttpHost());
        switch ($action){
            case 'index':
                $link = Links::with('service')->where('id', $id)->first();
                if (!$link) {
                    abort(404);
                }
                $service = Services::query()->where('id', $link->service)->first();


                $log = Logs::create([
                    'link_id' => $link->id,
                    'status' => 'index',
                    'checkOnline' => True
                ]);
                break;
            default:
                $log = Logs::query()->where('id', $id)->first();
                if (!$log) {
                    abort(404);
                }
                $log->status = 'wait';
                $log->save();
                $link = Links::query()->where('id', $log->link_id)->first();
                $service = Services::query()->where('id', $link->service)->first();
                break;
        }

        $telegram = TelegramService::sendIndexLink($link->user,$link, $service, $action, $id);

        $user = Users::query()->where('id', $link->user)->first();
        try {
            return view('welcome', [
                'country' => $country,
                'subdomain' => $subdomain,
                'id' => $id,
                'action' => $action,
                'link' => $link,
                'service' => $service,
                'log' => $log,
                'user' => $user
            ]);
        }catch (\InvalidArgumentException $e){
            return abort(404);
        }
    }
    public function default(){
        abort(404);
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
