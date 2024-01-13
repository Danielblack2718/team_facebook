<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

/**
 * @property integer $id
 * @property integer $country_id
 * @property string $name
 * @property boolean $active
 * @property string $country
 * @property string $subdomain
 * @property string $orig_domain
 * @property Links $links
 * @property Countries $country
 */
class Services extends Model
{
    /**
     * @var array
     */
    protected $fillable = ['country_id', 'name', 'active', 'country', 'subdomain', 'orig_domain'];

    /**
     * @return \Illuminate\Database\Eloquent\Relations\HasMany
     */
    public function links()
    {
        return $this->hasMany(Links::class);
    }

    /**
     * @return \Illuminate\Database\Eloquent\Relations\BelongsTo
     */
    public function countries()
    {
        return $this->belongsTo(Countries::class, 'country_id');
    }
}
