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
            $table->boolean('first_profit')->default(1);
            $table->timestamps();
            $table->tinyInteger('mentor')->default(0);
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('users');
    }
};
