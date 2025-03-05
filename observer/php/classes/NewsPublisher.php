<?php

class NewsPublisher implements Subject {
    private $observers = [];
    private $latestNews = '';

    public function attach(Observer $observer) {
        $this->observers[] = $observer;
    }

    public function detach(Observer $observer) {
        $key = array_search($observer, $this->observers, true);
        if ($key !== false) {
            unset($this->observers[$key]);
        }
    }

    public function notify() {
        foreach ($this->observers as $observer) {
            $observer->update($this->latestNews);
        }
    }

    public function publishNews($news) {
        $this->latestNews = $news;
        $this->notify();
    }
}