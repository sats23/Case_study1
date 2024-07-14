from openai import OpenAI

# Initialize OpenAI client with your API key
client = OpenAI(
  api_key="YOUR_API_KEY",  # Replace with your actual OpenAI API key
)

# Predefined responses for common questions
questions_answers = [
    ["How can I reset my password?", "You can reset your password by clicking on 'Forgot Password' on the login page."],
    ["Where is my order?", "You can track your order status in the 'My Orders' section of your account."],
    ["How do I contact customer support?", "You can contact customer support through our 'Contact Us' page or call us at 123-456-7890."],
    ["What is your return policy?", "You can return any item within 30 days of purchase as long as it is in its original condition."],
    ["How do I update my billing information?", "You can update your billing information in the 'Payment Methods' section of your account settings."],
    ["Can I change my shipping address?", "You can change your shipping address in the 'Address Book' section of your account."],
    ["Why is my account locked?", "Your account may be locked due to multiple failed login attempts. Please reset your password or contact support."],
    ["How do I apply a discount code?", "You can apply a discount code at checkout in the 'Promo Code' field."],
    ["What payment methods do you accept?", "We accept all major credit cards, PayPal, and bank transfers."],
    ["How do I cancel my order?", "You can cancel your order within 24 hours of placing it from the 'My Orders' section."],
    ["When will my order arrive?", "Delivery times vary based on your location and shipping method selected at checkout."],
    ["How can I track my shipment?", "You can track your shipment using the tracking number provided in your confirmation email."],
    ["What if my item is damaged or defective?", "Please contact customer support immediately for assistance with damaged or defective items."],
    ["How do I change my subscription plan?", "You can change your subscription plan in the 'Subscriptions' section of your account settings."],
    ["Can I get a refund?", "Refunds are processed within 5-7 business days after we receive your return."],
    ["How do I update my profile information?", "You can update your profile information in the 'Account Settings' section of your account."],
    ["Why was my payment declined?", "Payments can be declined for various reasons. Please check your payment details or contact your bank."],
    ["Do you ship internationally?", "Yes, we ship to many countries. Please check our shipping policy for more details."],
    ["How do I subscribe to your newsletter?", "You can subscribe to our newsletter at the bottom of our homepage."],
    ["Can I return an item I bought on sale?", "Yes, sale items can be returned within 30 days of purchase."],
    ["How do I delete my account?", "Please contact customer support to request account deletion."],
    ["What are your customer service hours?", "Our customer service is available 24/7."],
    ["How can I provide feedback?", "You can provide feedback through our 'Contact Us' page."],
    ["Do you have a loyalty program?", "Yes, we have a loyalty program. You can join in the 'Rewards' section of your account."],
    ["Can I update my order?", "You can update your order within 24 hours of placing it from the 'My Orders' section."],
    ["How do I change my password?", "You can change your password in the 'Account Settings' section of your account."],
    ["Can I combine multiple discount codes?", "Only one discount code can be applied per order."],
    ["What is the warranty on your products?", "Our products come with a one-year warranty. Please check the product page for specific details."],
    ["How do I redeem my gift card?", "You can redeem your gift card at checkout in the 'Gift Card' field."],
    ["Can I pick up my order in-store?", "Yes, you can choose in-store pickup at checkout."],
    ["How do I find my order number?", "Your order number is in the confirmation email we sent you."],
    ["What is your exchange policy?", "You can exchange items within 30 days of purchase."],
    ["How do I download my invoice?", "You can download your invoice from the 'My Orders' section of your account."],
    ["How do I report a problem with my order?", "Please contact customer support to report any issues with your order."],
    ["Can I change the email address on my account?", "Yes, you can change your email address in the 'Account Settings' section."],
    ["What is your privacy policy?", "You can read our privacy policy on our website under 'Privacy Policy'."],
    ["How do I apply for a job at your company?", "You can view and apply for job openings on our 'Careers' page."],
    ["Do you offer free shipping?", "We offer free shipping on orders over a certain amount. Please check our shipping policy for details."],
    ["How do I verify my email address?", "We will send you a verification email after you register. Please click the link in the email to verify your address."],
    ["How do I change my communication preferences?", "You can change your communication preferences in the 'Account Settings' section of your account."],
    ["Why didn't I receive a confirmation email?", "Please check your spam folder. If you still haven't received it, contact customer support."],
    ["Can I reorder an item I previously purchased?", "Yes, you can reorder items from the 'My Orders' section of your account."],
    ["How do I view my order history?", "You can view your order history in the 'My Orders' section of your account."],
    ["Can I add items to an existing order?", "Once an order is placed, you cannot add items to it. You will need to place a new order."],
    ["What should I do if I receive the wrong item?", "Please contact customer support to resolve the issue."],
    ["How do I update my shipping information?", "You can update your shipping information in the 'Address Book' section of your account."],
    ["Can I save items for later?", "Yes, you can save items to your wishlist for future purchase."],
    ["How do I unsubscribe from your emails?", "You can unsubscribe by clicking the 'Unsubscribe' link at the bottom of any of our emails."],
    ["Why is my order delayed?", "Orders can be delayed due to various reasons such as high demand or shipping issues. Please check your order status for updates."],
    ["How do I apply for a refund?", "You can request a refund through the 'My Orders' section of your account."],
    ["What is your cancellation policy?", "You can cancel your order within 24 hours of placing it."],
    ["How do I know if an item is in stock?", "The product page will indicate if an item is in stock."],
    ["Can I change my order after it has been shipped?", "Once an order has been shipped, it cannot be changed."],
    ["How do I find my size?", "You can refer to our size guide on the product page."],
    ["What if I entered the wrong shipping address?", "Please contact customer support immediately to correct the shipping address."],
    ["Can I expedite my shipping?", "Yes, you can choose expedited shipping at checkout."],
    ["How do I leave a review?", "You can leave a review on the product page under 'Customer Reviews'."],
    ["How do I report a website issue?", "Please contact customer support to report any website issues."],
    ["How do I change my payment method?", "You can change your payment method in the 'Payment Methods' section of your account."],
    ["What is your security policy?", "We take your security seriously. Please read our security policy on our website."],
    ["How do I set up an account?", "You can set up an account by clicking on 'Sign Up' and providing the required information."],
    ["How do I apply for a business account?", "You can apply for a business account on our 'Business' page."],
    ["Do you offer gift wrapping?", "Yes, we offer gift wrapping at checkout."],
    ["How do I reset my security questions?", "You can reset your security questions in the 'Account Settings' section."],
    ["Can I update my phone number?", "Yes, you can update your phone number in the 'Account Settings' section."],
    ["How do I manage my notifications?", "You can manage your notifications in the 'Account Settings' section."],
    ["What is your environmental policy?", "You can read about our environmental policy on our website."],
    ["How do I find a store near me?", "You can use our store locator on our website to find a store near you."],
    ["Can I use multiple shipping addresses?", "Yes, you can add multiple shipping addresses in the 'Address Book' section of your account."],
    ["How do I join your affiliate program?", "You can join our affiliate program through our 'Affiliate' page."],
    ["How do I know if my payment was successful?", "You will receive a confirmation email once your payment is successful."],
    ["Can I order out-of-stock items?", "Out-of-stock items cannot be ordered, but you can sign up for notifications when they are back in stock."],
    ["How do I subscribe to your magazine?", "You can subscribe to our magazine on our 'Magazine' page."],
    ["What are your business hours?", "Our business hours are Monday to Friday, 9 AM to 5 PM."],
]

def find_predefined_answer(question):
    for q, a in questions_answers:
        if q.lower() in question.lower():
            return a
    return None

def generate_response(prompt):
    predefined_answer = find_predefined_answer(prompt)
    if predefined_answer:
        return predefined_answer
    
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful customer support assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content

# Example usage
if __name__ == "__main__":
    prompt = "How can I reset my password?"
    response = generate_response(prompt)
    print(response)
