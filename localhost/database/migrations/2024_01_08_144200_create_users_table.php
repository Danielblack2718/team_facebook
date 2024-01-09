<?php
use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateUsersTable1 extends Migration
{
    public function up()
    {
        Schema::create('users', function (Blueprint $table) {
            $table->bigIncrements('id');
            $table->text('username');
            $table->tinyInteger('hide')->default(0);
            $table->text('ref');
            $table->tinyInteger('supportChat')->nullable();
            $table->text('supportChatApi')->nullable();
            $table->tinyInteger('confirmed')->default(1);
            $table->tinyInteger('banned')->default(0);
            $table->tinyInteger('admin')->default(0);
            $table->string('nickname', 30);
            $table->text('status');
            $table->timestamps();
            $table->tinyInteger('mentor')->default(0);
        });
    }

    public function down()
    {
        Schema::dropIfExists('users');
    }
}
