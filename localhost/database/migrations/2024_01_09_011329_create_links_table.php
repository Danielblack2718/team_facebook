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
        Schema::create('links', function (Blueprint $table) {
            $table->id();
            $table->text('name');
            $table->text('price');
            $table->text('description');
            $table->unsignedBigInteger('service');
            $table->tinyInteger('checker')->default(0);
            $table->text('photo')->nullable();
            $table->text('address');
            $table->text('author');
            $table->text('number');
            $table->unsignedBigInteger('user');

            $table->timestamps();
        });

        Schema::table('links', function (Blueprint $table) {
            $table->foreign('service')->references('id')->on('services')->onDelete('cascade');
            $table->foreign('user')->references('id')->on('users')->onDelete('cascade');
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('links');
    }
};
