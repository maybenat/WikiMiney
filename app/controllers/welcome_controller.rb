class WelcomeController < ApplicationController
  $months = []
  $months.unshift(['October', '10'])
  $months.unshift(['November', '11'])
  $months.unshift(['December', '12'])

  $days = []
  for i in 1..31
    $days.unshift(['%d' i, '%d' i])
  end
  $days.unshift(['Entire Month Aggregate', 'all'])

  $years = []
  $years.unshift(['2008', '2008'])
  $years.unshift(['2012', '2012'])

  def index
  end

  def top
  end

  def compare
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
