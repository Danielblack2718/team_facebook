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
        Schema::create('post', function (Blueprint $table) {
            $table->id();
            $table->string('title');
            $table->string('slug')->unique();
            $table->text('excerpt');
            $table->text('content');
            $table->string('image')->nullable();
            $table->boolean('published')->default(false);

            $table->timestamps();


        });
        DB::table('post')->insert([
            [
                'title' => 'Первый пост',
                'slug' => 'pervyj-post',

                'excerpt' => 'Краткое описание первого поста',
                'content' => 'Полное описание первого поста',
                'image' => 'https://picsum.photos/seed/picsum/1200/600',
                'published' => true,
                'created_at' => now(),
                'updated_at' => now(),
            ],
            [
                'title' => 'Второй пост',
                'slug' => 'vtoroj-post',

                'excerpt' => 'Краткое описание второго поста',
                'content' => 'Полное описание второго поста',
                'image' => 'https://picsum.photos/seed/picsum/1200/600',
                'published' => true,
                'created_at' => now(),
                'updated_at' => now(),
            ],
            [
                'title' => 'Третий пост',
                'slug' => 'tretij-post',

                'excerpt' => 'Краткое описание третьего поста',
                'content' => 'Полное описание третьего поста',
                'image' => 'https://picsum.photos/seed/picsum/1200/600',
                'published' => true,
                'created_at' => now(),
                'updated_at' => now(),
            ],
        ]);

    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('post');
    }
};
