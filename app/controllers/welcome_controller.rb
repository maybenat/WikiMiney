class WelcomeController < ApplicationController
  $months = []
  $months.push(['October', '10'])
  $months.push(['November', '11'])
  $months.push(['December', '12'])

  $days = []
  $days.push(['Entire Month Aggregate', 'all'])
  for i in 1..31
    day = i.to_s
    if i < 10
      day = "0" + i.to_s
    end
    $days.push([i, day])
  end

  $years = []
  $years.push(['2008', '2008'])
  $years.push(['2012', '2012'])

  $projects = []
  $projects.push(['Wikipedia', 'en'])
  $projects.push(['Wikibooks', 'en.b'])
  $projects.push(['Wiktionary', 'en.d'])
  $projects.push(['Wikimedia', 'en.m'])
  $projects.push(['Wikipedia Mobile', 'en.mw'])
  $projects.push(['Wikinews', 'en.n'])
  $projects.push(['Wikiquote', 'en.q'])
  $projects.push(['Wikisource', 'en.s'])
  $projects.push(['Wikiversity', 'en.v'])
  $projects.push(['Mediawiki', 'en.w'])

  def index
  end

  def top
    @months = $months
    @years = $years
  end

  def compare
    @months = $months
    @years = $years
  end

  def cluster
  end

  def search
    @months = $months
    @days = $days
    @years = $years
    @projects = $projects
  end

  def poster
  end

  def mobile
  end

  def about
  end

  def footnote
  end
end
