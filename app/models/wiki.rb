class Wiki < ActiveRecord::Base
  validates :project, presence: true
  validates :page, presence: true
  validates :views, presence: true
  validates :bytes, presence: true
end
