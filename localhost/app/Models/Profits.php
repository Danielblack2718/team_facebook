<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

/**
 * @property integer $id
 * @property integer $amount
 * @property string $status
 * @property integer $user_id
 */
class Profits extends Model
{
    /**
     * @var array
     */
    protected $fillable = ['amount', 'status', 'user_id'];
}
