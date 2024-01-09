<?php
use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateProfitsTable1 extends Migration
{
    public function up()
    {
        Schema::create('profits', function (Blueprint $table) {
            $table->id();
            $table->integer('amount');
            $table->text('status');
            $table->bigInteger('user_id');
            $table->timestamps();
        });
    }

    public function down()
    {
        Schema::dropIfExists('profits');
    }
}
