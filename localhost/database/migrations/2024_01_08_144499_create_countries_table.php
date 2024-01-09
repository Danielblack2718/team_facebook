<?php
use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateCountriesTable1 extends Migration
{
    public function up()
    {
        Schema::create('countries', function (Blueprint $table) {
            $table->id();
            $table->text('name');
            $table->text('flag');
            $table->tinyInteger('active')->default(1);
        });

        // Вставляем данные о странах из вашего SQL-дампа
        DB::table('countries')->insert([
            [
                'name' => 'Венгрия',
                'flag' => '🇭🇺',
                'active' => 1,
            ],
            [
                'name' => 'Австрия',
                'flag' => '🇦🇹',
                'active' => 1,
            ],
            // Добавьте другие страны, перечисляя их здесь
        ]);

    }

    public function down()
    {
        Schema::dropIfExists('countries');
    }
}

