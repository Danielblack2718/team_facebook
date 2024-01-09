<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

/**
 * @property integer $id
 * @property integer $user_id
 * @property string $username
 * @property string $type
 * @property string $textType
 * @property string $status
 * @property string $created_at
 * @property integer $message_id
 */
class Requests extends Model
{
    /**
     * @var array
     */
    protected $fillable = ['user_id', 'username', 'type', 'textType', 'status', 'created_at', 'message_id'];
}
