-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Дек 28 2023 г., 00:28
-- Версия сервера: 5.7.39
-- Версия PHP: 8.1.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `bot`
--

-- --------------------------------------------------------

--
-- Структура таблицы `countries`
--

CREATE TABLE `countries` (
  `id` int(11) NOT NULL,
  `name` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `flag` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `active` tinyint(1) NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Дамп данных таблицы `countries`
--

INSERT INTO `countries` (`id`, `name`, `flag`, `active`) VALUES
(1, 'Венгрия', '🇭🇺', 1),
(2, 'Австрия', '🇦🇹', 1);

-- --------------------------------------------------------

--
-- Структура таблицы `links`
--

CREATE TABLE `links` (
  `id` int(11) NOT NULL,
  `name` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `price` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `service` int(11) NOT NULL,
  `checker` tinyint(1) NOT NULL DEFAULT '0',
  `photo` text COLLATE utf8mb4_unicode_ci,
  `address` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `author` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `number` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `user` bigint(11) NOT NULL,
  `admin_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Дамп данных таблицы `links`
--

INSERT INTO `links` (`id`, `name`, `price`, `description`, `service`, `checker`, `photo`, `address`, `author`, `number`, `user`, `admin_id`) VALUES
(2, '423', '423', '4', 3, 0, '25', '534', '234', '', 0, 0),
(3, '55', '345', '43', 3, 0, '534', '5', '534', '', 0, 0),
(4, '4234', '423', '43', 1, 1, '324', '23', '24', '', 0, 0),
(5, '34534', '53', '45', 3, 0, '0', '423432', '53453', '4234', 0, 0),
(6, '423432', '423423', '4324', 3, 0, '4234', '423423', '42342', '42342', 0, 0),
(7, '42342354', '52345', '5', 1, 0, '324', '423', '2345', '534', 0, 0),
(8, '5324', '52', '345', 3, 0, '234', '534', '345', '534', 0, 0),
(9, '423432', '534534', '534534', 1, 0, '534', '345', '5345', '5345', 0, 0),
(10, '42342', '42', '34', 1, 1, '42', '3', '2', '432', 0, 0),
(11, '423', '423', '4', 3, 1, '432', '4234', '23', '432', 0, 0),
(12, '423432', '423', '423', 1, 1, '34', '43', '4', '234', 0, 0),
(13, '4123432', '52345342', '5534534', 1, 0, '345', '534', '5', '34', 0, 0),
(14, '42342', '4', '23', 4, 0, '4234', '423', '423', '23', 0, 0),
(15, '432', '564322', '423', 1, 0, '432', '4', '423', '432', 0, 0),
(16, '423', '4325', '34', 1, 1, '534', '423', '534', '423', 0, 0),
(17, '4234324', '234', '23', 1, 1, '4', '324', '423', '234', 0, 0),
(18, '43252345234', '534', '5', 2, 0, '34', '534', '345', '534', 0, 0),
(25, '53454', '5', '34', 2, 0, '534', '534', '54', '534534', 6970026013, NULL),
(26, '4', '234', '32', 2, 0, '423', '3', '423', '42', 6970026013, NULL),
(27, '43242', '423', '432', 4, 0, '324', '432', '4', '32', 6970026013, NULL);

-- --------------------------------------------------------

--
-- Структура таблицы `services`
--

CREATE TABLE `services` (
  `id` int(11) NOT NULL,
  `name` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `country_id` int(11) NOT NULL,
  `active` tinyint(1) NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Дамп данных таблицы `services`
--

INSERT INTO `services` (`id`, `name`, `country_id`, `active`) VALUES
(1, 'Facebook', 1, 1),
(2, 'JOFOGAS', 2, 1),
(3, 'Facebook', 2, 1),
(4, 'Willhaben', 1, 1);

-- --------------------------------------------------------

--
-- Структура таблицы `users`
--

CREATE TABLE `users` (
  `id` bigint(20) NOT NULL,
  `username` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `hide` tinyint(1) NOT NULL DEFAULT '0',
  `ref` text COLLATE utf8mb4_unicode_ci,
  `supportChat` tinyint(1) DEFAULT NULL,
  `supportChatApi` text COLLATE utf8mb4_unicode_ci,
  `confirmed` tinyint(1) NOT NULL DEFAULT '1',
  `banned` tinyint(1) NOT NULL DEFAULT '0',
  `admin` tinyint(1) NOT NULL DEFAULT '0',
  `balance` tinyint(1) DEFAULT NULL,
  `nickname` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Дамп данных таблицы `users`
--

INSERT INTO `users` (`id`, `username`, `hide`, `ref`, `supportChat`, `supportChatApi`, `confirmed`, `banned`, `admin`, `balance`, `nickname`) VALUES
(612475751, 'dblackq', 0, 'None', 1, NULL, 1, 0, 0, 0, 'gsdfgsdf'),
(6970026013, 'dblackq_second', 0, '@gethhj', 1, 'dfgsg45g', 1, 0, 1, NULL, 'aaaaaa');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `countries`
--
ALTER TABLE `countries`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `links`
--
ALTER TABLE `links`
  ADD PRIMARY KEY (`id`),
  ADD KEY `service` (`service`);

--
-- Индексы таблицы `services`
--
ALTER TABLE `services`
  ADD PRIMARY KEY (`id`),
  ADD KEY `country_id` (`country_id`);

--
-- Индексы таблицы `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nickname` (`nickname`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `countries`
--
ALTER TABLE `countries`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT для таблицы `links`
--
ALTER TABLE `links`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT для таблицы `services`
--
ALTER TABLE `services`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `links`
--
ALTER TABLE `links`
  ADD CONSTRAINT `links_ibfk_1` FOREIGN KEY (`service`) REFERENCES `services` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ограничения внешнего ключа таблицы `services`
--
ALTER TABLE `services`
  ADD CONSTRAINT `services_ibfk_1` FOREIGN KEY (`country_id`) REFERENCES `countries` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
