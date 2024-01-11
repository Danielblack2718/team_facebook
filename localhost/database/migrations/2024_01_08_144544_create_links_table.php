<?php
use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateLinksTable1 extends Migration
{
    public function up()
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
            $table->unsignedBigInteger('admin_id')->nullable();
            $table->timestamps();
        });

        Schema::table('links', function (Blueprint $table) {
            $table->foreign('service')->references('id')->on('services')->onDelete('cascade');
            $table->foreign('user')->references('id')->on('users')->onDelete('cascade');
        });
    }

    public function down()
    {
        Schema::dropIfExists('links');
    }
}