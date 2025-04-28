<?php

namespace Tests\Feature;

use Tests\TestCase;

class LandingPageTest extends TestCase
{
    public function test_landing_page_youtube_video_is_visible()
    {
        $response = $this->get('/');

        $response->assertStatus(200);
        $response->assertSee('https://www.youtube.com/watch?v=C2AmVFZLyf4');
    }
}
