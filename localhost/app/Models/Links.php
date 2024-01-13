<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

/**
 * @property integer $id
 * @property integer $service
 * @property integer $user
 * @property string $name
 * @property string $price
 * @property string $description
 * @property boolean $checker
 * @property string $photo
 * @property string $address
 * @property string $author
 * @property string $number
 * @property integer $admin_id
 * @property Services $service
 * @property Users $user
 */
class Links extends Model
{
    protected $with = ['service'];
    /**
     * @var array
     */
    protected $fillable = ['service','uniq_id', 'user', 'name', 'price', 'description', 'checker', 'photo', 'address', 'author', 'number', 'admin_id'];



    /**
     * @return \Illuminate\Database\Eloquent\Relations\BelongsTo
     */
    public function service()
    {
        return $this->belongsTo(Services::class, 'service');
    }

    /**
     * @return \Illuminate\Database\Eloquent\Relations\BelongsTo
     */
    public function user()
    {
        return $this->belongsTo(Users::class);
    }

    public function logs()
    {
        return $this->hasMany(Logs::class, 'link_id');
    }
}
