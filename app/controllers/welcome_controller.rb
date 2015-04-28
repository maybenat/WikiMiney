class WelcomeController < ApplicationController
  $months = []
  $months.push(['October', '10'])
  $months.push(['November', '11'])
  $months.push(['December', '12'])

  $days = []
  for i in 1..31
    $days.push([i, i])
  end
  $days.push(['Entire Month Aggregate', 'all'])

  $years = []
  $years.push(['2008', '2008'])
  $years.push(['2012', '2012'])

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
  end

  def poster
  end

  def about
  end

  def mobile
  end
end
