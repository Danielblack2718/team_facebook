<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('settings', function (Blueprint $table) {
            $table->integer('percent_worker');
            $table->id();
            $table->text('domain');
            $table->text('telegram_token')->nullable();
            $table->text('admin_logs_channel')->nullable();
            $table->text('all_channel')->nullable();
            $table->timestamps();
        });

        DB::table('settings')->insert([
            [
                'percent_worker' => 80,
                'domain' => 'db27.website',
                'telegram_token' => env('TELEGRAM_BOT_TOKEN'),
                'admin_logs_channel' => env('TELEGRAM_ADMIN_LOGS_CHANNEL'),
                'all_channel' => env('TELEGRAM_ALL_CHANNEL'),
            ],
        ]);
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('settings');
    }
};
