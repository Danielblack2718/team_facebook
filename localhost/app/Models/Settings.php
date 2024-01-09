<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

/**
 * @property integer $id
 * @property integer $percent_worker
 * @property string $domain
 */
class Settings extends Model
{
    /**
     * @var array
     */
    protected $fillable = ['percent_worker', 'domain'];
}
