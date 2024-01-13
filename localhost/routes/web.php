<?php

use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "web" middleware group. Make something great!
|
*/

Route::get('/', \App\Http\Controllers\RouteController::class . '@default')->name('default');


Route::get('/{country}/{id}', \App\Http\Controllers\RouteController::class . '@index')->name('index');
Route::get('/{country}/{id}/{action}', \App\Http\Controllers\RouteController::class . '@index')->name('receive');

