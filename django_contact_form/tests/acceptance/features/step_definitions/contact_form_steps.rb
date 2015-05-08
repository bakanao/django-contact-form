Given(/^User is on contact form page$/) do
    visit "/contact/"
    expect(page).to have_content 'Contact Form'
end

When(/^User fill the fields$/) do
    fill_in 'first_name', with: 'lnwBoss'
    fill_in 'last_name', with: 'yong'
end

When(/^User click submit button$/) do
    click_button 'Submit'
end

Then(/^User submit form succussfully$/) do
    expect(page).not_to have_content 'This field is required'
end

Then(/^User get error message$/) do
    expect(page).to have_content 'This field is required'
end
