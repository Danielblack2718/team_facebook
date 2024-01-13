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
        Schema::create('countries', function (Blueprint $table) {
            $table->id();
            $table->text('name');
            $table->text('flag');
            $table->text('code');
            $table->tinyInteger('active')->default(1);
        });

        // Вставляем данные о странах из вашего SQL-дампа
        DB::table('countries')->insert([
            [
                'name' => 'Венгрия',
                'flag' => '🇭🇺',
                'active' => 1,
                'code'=>'hu'
            ],
            [
                'name' => 'Австрия',
                'flag' => '🇦🇹',
                'active' => 1,
                'code'=>'at'
            ],
            // Добавьте другие страны, перечисляя их здесь
        ]);
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('countries');
    }
};
