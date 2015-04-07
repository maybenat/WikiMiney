class Wikipage < ActiveRecord::Base
  validates :project, presence: true
  validates :page, presence: true
  has_many :wikiviews, dependent: :destroy
end


class Wikiview < ActiveRecord::Base
  belongs_to :wikipage
  validates :year, presence: true
  validates :month, presence: true
  validates :day, presence: true
  validates :views, presence: true
  validates :bytes, presence: true
end
