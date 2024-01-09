<?php
use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateSettingsTable1 extends Migration
{
    public function up()
    {
        Schema::create('settings', function (Blueprint $table) {
            $table->integer('percent_worker');
            $table->id();
            $table->text('domain');
            $table->timestamps();
        });
    }

    public function down()
    {
        Schema::dropIfExists('settings');
    }
}
