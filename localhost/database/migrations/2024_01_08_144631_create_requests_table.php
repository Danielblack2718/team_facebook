<?php
use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateRequestsTable1 extends Migration
{
    public function up()
    {
        Schema::create('requests', function (Blueprint $table) {
            $table->id();
            $table->bigInteger('user_id');
            $table->text('username');
            $table->text('type');
            $table->text('textType')->nullable();
            $table->text('status');
            $table->timestamps();
            $table->bigInteger('message_id')->nullable();
        });
    }

    public function down()
    {
        Schema::dropIfExists('requests');
    }
}
