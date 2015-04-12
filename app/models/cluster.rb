class Cluster < ActiveRecord::Base
  validates :project, presence: true
  validates :page, presence: true
  validates :year, presence: true
  validates :month, presence: true
  validates :views, presence: true
  validates :bytes, presence: true
  validates :cluster, presence: true
end
