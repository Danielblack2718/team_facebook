<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

/**
 * @property integer $id
 * @property string $name
 * @property string $flag
 * @property boolean $active
 * @property Services $services
 */
class Countries extends Model
{
    /**
     * @var array
     */
    protected $fillable = ['name', 'flag', 'active'];

    /**
     * @return \Illuminate\Database\Eloquent\Relations\HasMany
     */
    public function services()
    {
        return $this->hasMany(Services::class);
    }
}
