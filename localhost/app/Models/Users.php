<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

/**
 * @property integer $id
 * @property string $username
 * @property boolean $hide
 * @property string $ref
 * @property boolean $supportChat
 * @property string $supportChatApi
 * @property boolean $confirmed
 * @property boolean $banned
 * @property boolean $admin
 * @property string $nickname
 * @property string $status
 * @property string $added
 * @property boolean $mentor
 * @property Links $links
 */
class Users extends Model
{
    /**
     * Indicates if the IDs are auto-incrementing.
     *
     * @var bool
     */
    public $incrementing = false;

    /**
     * @var array
     */
    protected $fillable = ['username', 'hide', 'ref', 'supportChat', 'supportChatApi', 'confirmed', 'banned', 'admin', 'nickname', 'status', 'added', 'mentor'];

    /**
     * @return \Illuminate\Database\Eloquent\Relations\HasMany
     */
    public function links()
    {
        return $this->hasMany('App\Models\Links', 'user');
    }
}
